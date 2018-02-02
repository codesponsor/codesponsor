import axios from 'axios';

/**
 * Config global for axios/django
 */
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

export default axios;