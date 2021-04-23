import { TypedUseSelectorHook, useSelector } from "react-redux";
import { ApplicationState } from "../types";

export const useStateSelector: TypedUseSelectorHook<ApplicationState> = useSelector;
export default useStateSelector;
