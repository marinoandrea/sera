import { useToast } from "@chakra-ui/react";
import useHttpService, {
  RequestState,
  Result,
  Service,
} from "use-http-service";
import { ErrorResponse } from "../types";
import useStateSelector from "./useStateSelector";

const UNKNOWN_ERROR = "Something went wrong, try again later.";

export default function useApi<R, D>(
  service: Service
): [
  RequestState<D, ErrorResponse>,
  (requestBody?: R) => Promise<Result<D, ErrorResponse>>
] {
  const { token } = useStateSelector((state) => state.auth);

  const toast = useToast();

  const [state, callApi] = useHttpService<R, D, ErrorResponse>({
    ...service,
    headers: {
      ...(service.headers || {}),
      Authorization: `Bearer ${token}`,
    },
  });

  const wrapper = async (body?: R) => {
    try {
      const res = await callApi(body);
      if (!res.isOk) {
        toast({
          status: "error",
          title: "Error",
          description: res.error.error,
          position: "top",
        });
      }
      return res;
    } catch (e) {
      console.log(e);

      toast({
        status: "error",
        title: "Error",
        description: UNKNOWN_ERROR,
        position: "top",
      });

      return {
        isOk: false,
        error: { error: UNKNOWN_ERROR },
      } as Result<D, ErrorResponse>;
    }
  };

  return [state, wrapper];
}
