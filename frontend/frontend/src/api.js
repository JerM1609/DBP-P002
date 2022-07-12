import axios from "axios";

const authService = axios.create({
  baseURL: "http://127.0.0.1:5001",
  withCredentials: true,
  xsrfCookieName: "X-CSRF-TOKEN-ACCESS",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    responseType: "json",
  },
});
export { authService };
