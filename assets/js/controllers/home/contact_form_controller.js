import { Controller } from 'stimulus';
import Noty from 'noty';
import axios from '../../axios';

export default class extends Controller {
  static targets = ["name", "email", "subject", "content"]

  connect() {
    console.log("Hello, Stimulus!", this.element);
  }

  submit(event) {
    if (!this.element.checkValidity()) {
      return false;
    }
    
    event.preventDefault(); // Do not submit form

    const name = this.nameTarget.value;
    const email = this.emailTarget.value;
    const subject = this.subjectTarget.value;
    const content = this.contentTarget.value;

    axios.post(this.element.action, {
      name, email, subject, content
    })
      .then(_response => {
        new Noty({
          type: "success",
          text: "Your message was sent successfully",
          timeout: 3500,
          progressBar: true,
        }).show();
      })
      .catch(_error => {
        new Noty({
          type: "error",
          text: "Oops! Your message was not sent",
          timeout: 3500,
          progressBar: true,
        }).show();
      });
  }
}
