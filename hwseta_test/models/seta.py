from odoo import _, api, fields, models

class Learners(models.Model):
	_name = 'hwseta.learners'

	name = fields.Char()
	id_number = fields.Char()
	# qualifications = fields.????


class Qualifications(models.Model):
	_name = 'hwseta.qualifications'

	def _get_total_credits(self):
		return 25

	name = fields.Char()
	# units = fields.???
	total_credit = fields.Integer(compute=_get_total_credits)


class Units(models.Model):
	_name = 'hwseta.units'

	name = fields.Char()
	credit = fields.Integer()

class LearnerQualifications(models.Model):
	_name = 'learner.qualifications'

	qualification = fields.Many2one('hwseta.qualifications')
	learner = fields.Many2one('hwseta.learners')
	#units = fields.Many2many('hwseta.units', related='qualification.units')

class LearnerUnits(models.Model):
	_name = 'learner.units'

	master_unit = fields.Many2one('hwseta.units')
	achieved = fields.Boolean()
