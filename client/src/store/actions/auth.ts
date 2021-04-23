import { StateAction, User } from "../../types";

export const LOGOUT = "LOGOUT";
export const LOGIN = "LOGIN";

export function login({
  user,
  token,
}: {
  user: User;
  token: string;
}): StateAction {
  return { type: LOGIN, payload: { user, token } };
}

export function logout(): StateAction {
  return { type: LOGOUT };
}
