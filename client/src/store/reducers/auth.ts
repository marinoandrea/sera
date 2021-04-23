import { AuthState, StateAction } from "../../types";
import { LOGIN, LOGOUT } from "../actions/auth";

const defaultAuthState: AuthState = {
  isAuthenticated: false,
  token: undefined,
  user: undefined,
};

export default function authReducer(
  state: AuthState = defaultAuthState,
  action: StateAction
) {
  switch (action.type) {
    case LOGIN:
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload.user,
        token: action.payload.token,
      };

    case LOGOUT:
      return {
        ...state,
        isAuthenticated: false,
        user: undefined,
        token: undefined,
      };

    default:
      return state;
  }
}
