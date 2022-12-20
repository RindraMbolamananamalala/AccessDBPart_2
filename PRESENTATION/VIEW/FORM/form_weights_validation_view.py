from PRESENTATION.HMI.FORM.form_weights_validation_ui import FormWeightsValidationUI

from PRESENTATION.VIEW.accessdb_pii_view import AccessDBPIIView


class FormWeightsValidationView(AccessDBPIIView):

    def __init__(self):
        #  First, let's call the Superclass' __init__() function
        super(FormWeightsValidationView, self).__init__()

        # Let us assign an Instance of the Form Weights Validation UI to the current VIEW
        self.set_corresponding_hmi(FormWeightsValidationUI(None))

    def feed_weights_to_confirm(self, weights_to_confirm: list):
        """
        Feeding all the Text Area corresponding to the Weights to be confirmed.
        :param weights_to_confirm: The list of Weights corresponding to each Category to be confirmed
        :return: None
        """
        hmi = self.get_corresponding_hmi()
        category_counter = 0
        for weight in weights_to_confirm:
            category_counter += 1
            if category_counter == 1:
                hmi.get_text_aluminijum().setText(weight)
            elif category_counter == 2:
                hmi.get_text_bakar().setText(weight)
            elif category_counter == 3:
                hmi.get_text_plastika().setText(weight)
            elif category_counter == 4:
                hmi.get_text_terminali().setText(weight)
            elif category_counter == 5:
                hmi.get_text_harness().setText(weight)



