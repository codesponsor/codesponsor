import { Application } from "stimulus";

import ContactFormController from "./controllers/home/contact_form_controller";

const application = Application.start();

application.register("contact-form", ContactFormController);
