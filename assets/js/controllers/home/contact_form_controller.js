import { Controller } from "stimulus";
import Noty from "noty";
import axios from "../../axios";

export default class extends Controller {
  static targets = ["name", "email", "subject", "content"];

  submit(event) {
    if (!this.element.checkValidity()) {
      return;
    }

    event.preventDefault(); // Do not submit form

    const name = this.nameTarget.value;
    const email = this.emailTarget.value;
    const subject = this.subjectTarget.value;
    const content = this.contentTarget.value;

    const success = () => {
      this.element.reset();

      new Noty({
        type: "success",
        text: "Your message was sent successfully",
        timeout: 3500,
        progressBar: true
      }).show();
    };

    const fail = () => {
      new Noty({
        type: "error",
        text: "Oops! Your message was not sent",
        timeout: 3500,
        progressBar: true
      }).show();
    };

    axios
      .post(this.element.action, {
        name,
        email,
        subject,
        content
      })
      .then(success.bind(this))
      .catch(fail.bind(this));
  }
}
