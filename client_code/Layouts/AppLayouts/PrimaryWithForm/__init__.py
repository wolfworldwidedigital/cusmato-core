import anvil.facebook.auth
import anvil.server
from ._anvil_designer import PrimaryWithFormTemplate

class PrimaryWithForm(PrimaryWithFormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
