import { useDispatch } from "react-redux";
import { Dispatch } from "redux";
import { StateAction } from "../types";

const useStateDispatch: () => Dispatch<StateAction> = useDispatch;
export default useStateDispatch;
