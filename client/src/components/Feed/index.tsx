import { Button } from "@chakra-ui/button";
import React, { useEffect } from "react";
import OfferingsAPI, {
  GetOfferingsLatestRequest,
  GetOfferingsLatestResponse,
} from "../../services/offerings";
import { logout } from "../../store/actions/auth";
import useApi from "../../utils/useApi";
import useStateDispatch from "../../utils/useStateDispatch";
import Container from "../common/Container";
import Loader from "../common/Loader";

interface FeedProps {}

const Feed: React.FC<FeedProps> = () => {
  const dispatch = useStateDispatch();

  const [{ isPending, data }, postOfferingsSearch] = useApi<
    GetOfferingsLatestRequest,
    GetOfferingsLatestResponse
  >(OfferingsAPI.buildGetOfferingsLatest());

  useEffect(() => {
    postOfferingsSearch();
  }, []);

  if (isPending) return <Loader />;

  return (
    <Container>
      <Button onClick={() => dispatch(logout())}>Sign Out</Button>
    </Container>
  );
};

export default Feed;
