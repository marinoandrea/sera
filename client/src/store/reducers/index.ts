import { combineReducers, Reducer } from "redux";
import storage from "redux-persist/lib/storage";
import { ApplicationState, StateAction } from "../../types";
import { LOGOUT } from "../actions/auth";
import { STORE_VERSION } from "../config";
import authReducer from "./auth";

const reducers = combineReducers({
  auth: authReducer,
});

// @ts-ignore
const rootReducer: Reducer<ApplicationState, StateAction> = (
  state: ApplicationState,
  action: StateAction
) => {
  if (action.type === LOGOUT) {
    storage
      .removeItem(`persist:root_${STORE_VERSION}`)
      .then((_) => console.log("[debug] logged out"));
    return reducers(undefined, action);
  }
  return reducers(state, action);
};

export default rootReducer;
