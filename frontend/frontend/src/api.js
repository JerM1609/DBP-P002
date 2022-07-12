import axios from "axios";
import router from "./router";

const authService = axios.create({
  baseURL: "http://127.0.0.1:5001",
  withCredentials: true,
  xsrfCookieName: "X-CSRF-TOKEN-ACCESS",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});
export { authService };

const COOKIE_EXPIRED_MSG = "Token has expired";
authService.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const error_message = error.response.data.msg;
    switch (error.response.status) {
      case 401:
        if (!error.config.retry && error_message === COOKIE_EXPIRED_MSG) {
          error.config.retry = true;
          authService.defaults.xsrfCookieName = "X-CSRF-TOKEN-REFRESH";
          await authService.post("/refresh_token");
          authService.defaults.xsrfCookieName = "X-CSRF-TOKEN-ACCESS";
          return authService(error.config);
        }
        break;
      case 404:
        router.push("/404");
        break;
      default:
        break;
    }
    return error.response;
  }
);
