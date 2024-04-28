from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, UserError



class Learners(models.Model):
	_name = 'hwseta.learners'

	name = fields.Char()
	id_number = fields.Char()
	qualifications = fields.One2many('learner.qualifications', 'learner')

	@api.onchange('id_number')
	def _onchange_id_number(self):
		if self.id_number:
			find_id = self.search([('id_number', '=', self.id_number)])
			if len(find_id) != 0:
				return {'warning': {'title': 'Invalid ID No ',
									'message': "ID No already exist in the System."
								  "Please Enter a different ID No."},
						'value': {'id_number': False}}




class Qualifications(models.Model):
	_name = 'hwseta.qualifications'
	_rec_name = 'name'

	@api.one
	@api.depends('units')
	def _get_total_credits(self):
		total_credit = 0
		for i in self.units:
			if i.credit:
				total_credit += int(i.credit)
		self.total_credit = total_credit

	name = fields.Char()
	units = fields.Many2many('hwseta.units', string='Units')
	total_credit = fields.Integer(compute=_get_total_credits)
	minimum_credits = fields.Integer()



class Units(models.Model):
	_name = 'hwseta.units'

	name = fields.Char()
	credit = fields.Integer()



class LearnerQualifications(models.Model):
	_name = 'learner.qualifications'

	qualification = fields.Many2one('hwseta.qualifications')
	learner = fields.Many2one('hwseta.learners')


	units = fields.One2many('learner.units', 'learner_qual_id', string='Units')
	#units = fields.Many2many('hwseta.units', related='qualification.units')
	achieved = fields.Boolean(default=False, compute='_compute_achieved')
	status = fields.Selection([('fail', 'Failed'), ('pass', 'Passed')], compute='_compute_status')
	min_credits = fields.Integer(related='qualification.minimum_credits')
	achieved_credits = fields.Integer(compute='_compute_achieved_credit')

	@api.one
	@api.depends('units')
	def _compute_achieved_credit(self):
		qual_units = self.units
		achived_units = 0
		if self.units:
			for i in qual_units:
				if i.achieved == True:
					achived_units += int(i.master_unit.credit)

			self.achieved_credits = achived_units

	@api.onchange('learner','qualification')
	def _onchange_check_existing_qual(self):
		if self.qualification and self.learner:
			exist_qual_list_ids = []
			try:
				for rec in self.learner.qualifications:
					if type(rec.id) == int:
						exist_qual_list_ids.append(rec.qualification.id)
			except:
				pass
			if self.qualification.id in exist_qual_list_ids:
				return {'warning': {'title': 'Invalid qualification ',
									'message': "Learner has alredy registered for this qualification."
											   "Please select another qualification."},
						'value': {'qualification': False}}


	@api.one
	@api.depends('achieved')
	def _compute_status(self):
		if self.achieved == True:
			self.status = 'pass'
		else:
			self.status = 'fail'

	@api.one
	@api.depends('units')
	def _compute_achieved(self):
		min_credit = self.qualification.minimum_credits
		qual_units = self.units
		achived_units = 0
		if self.units:
			for i in qual_units:
				if i.achieved == True:
					achived_units += int(i.master_unit.credit)
			if achived_units >= min_credit:
				self.achieved = True
			else:
				self.achieved = False






class LearnerUnits(models.Model):
	_name = 'learner.units'

	@api.multi
	def _get_assigned_user_field(self):
		# wdb.set_trace()

		unit_list = self.learner_qual_id.qualification.units.ids
		users = []
		for user in self.learner_qual_id.qualification.units:
				users.append(user.id)
		return [('id', 'in', unit_list)]


	master_unit = fields.Many2one('hwseta.units', domain="[('id', 'in', allowed_value_ids)]")
	achieved = fields.Boolean(default=False)
	learner_qual_id = fields.Many2one('learner.qualifications')
	master_unit_credit = fields.Integer(compute='_get_credits', store=True, string="Credit")

	allowed_value_ids = fields.Many2many(comodel_name="hwseta.units", compute="_compute_allowed_value_ids")

	@api.one
	@api.depends("master_unit")
	def _compute_allowed_value_ids(self):
		filtered_unit_ids = self.learner_qual_id.qualification.units.ids
		try:
			if self.learner_qual_id.units:
				for rec in self.learner_qual_id.units:
					filtered_unit_ids.remove(rec.master_unit.id)
		except:
			pass
		for record in self:
			record.allowed_value_ids = self.env["hwseta.units"].search([('id', 'in', filtered_unit_ids)])


	@api.one
	@api.depends('master_unit')
	def _get_credits(self):
		if self.master_unit.credit:
			self.master_unit_credit = int(self.master_unit.credit)

