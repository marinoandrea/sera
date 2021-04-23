import { Service } from "use-http-service";
import { API_ENDPOINT } from "../config";
import { SuccessResponse, User } from "../types";

const ROUTE = `${API_ENDPOINT}/users`;

export const UsersAPI = {
  buildPostUsers: (): Service => ({
    url: `${ROUTE}/`,
    method: "POST",
  }),
};

export default UsersAPI;

export type PostUsersRequest = {
  name: string;
  email: string;
  password: string;
  phone_number: string;
};
export type PostUsersResponse = SuccessResponse<{
  user: User;
  token: string;
}>;
