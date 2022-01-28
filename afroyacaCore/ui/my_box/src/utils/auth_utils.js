const axios = require("axios");


export const initAxios = () => {

  if (localStorage.hasOwnProperty("appToken")) {
    window.axios = axios.create({
      baseURL: window.location.origin,
      // timeout: 1000,
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token " + localStorage.getItem("appToken")
      }
    });
    window.file_axios = axios.create({
      baseURL: window.location.origin,
      // timeout: 1000,
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: "Token " + localStorage.getItem("appToken")
      }
    });
  } else {
    window.axios = axios.create({
      baseURL: window.location.origin,
      headers: {
        "Content-Type": "application/json"
      }
    });
    window.file_axios = axios.create({
      baseURL: window.location.origin,
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }
};