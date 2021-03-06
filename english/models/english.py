
from odoo import fields, models


class EnglishLexicon(models.Model):

    _name = 'english.lexicon'
    _description = 'english lexicon'

    word = fields.Char(string="Word", required=True, index=True)
    lexicon_explain_ids = fields.One2many('english.lexicon.explain', 'english_lexicon_id', "Detail")
    america_accent = fields.Char(string="America Accent")
    british_accent = fields.Char(string="British Accent")
    chinese_mean = fields.Text(string="Chinese Mean")
    america_voice_url = fields.Char(string="America URL")
    british_voice_url = fields.Char(string="British URL")
    source_name = fields.Char(string="From")
    sequence = fields.Integer()
    is_updated = fields.Boolean(string="Is Updated", default=False)


class EnglishLexiconExplain(models.Model):

    _name = 'english.lexicon.explain'
    _description = 'english lexicon explain'

    english_lexicon_id = fields.Many2one('english.lexicon', 'EnglishLexicon', ondelete='cascade', required=True)
    order = fields.Integer()
    raw_html_mean = fields.Text(string="Html Mean")
    gram = fields.Char(string="Gram")
    english_mean = fields.Text(string="Processed Mean")
    chinese_mean = fields.Text(string="Chinese Mean")
    is_format = fields.Boolean(string="Is Format", default=False)




