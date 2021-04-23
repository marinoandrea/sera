import { Service } from "use-http-service";
import { API_ENDPOINT } from "../config";
import { SuccessResponse, User } from "../types";

const ROUTE = `${API_ENDPOINT}/auth`;

export const AuthAPI = {
  buildPostLogin: (): Service => ({
    url: `${ROUTE}/login`,
    method: "POST",
  }),
};

export default AuthAPI;

export type PostAuthLoginRequest = {
  email: string;
  password: string;
};
export type PostAuthLoginResponse = SuccessResponse<{
  user: User;
  token: string;
}>;
