import { Box } from "@chakra-ui/layout";
import React, { useEffect } from "react";
import OfferingsAPI, {
  GetOfferingsLatestRequest,
  GetOfferingsLatestResponse,
} from "../../services/offerings";
import useApi from "../../utils/useApi";
import useStateSelector from "../../utils/useStateSelector";
import Container from "../common/Container";
import Loader from "../common/Loader";
import Title from "../common/typography/Title";
import FeedList from "./List";

interface FeedProps {}

const Feed: React.FC<FeedProps> = () => {
  const { user } = useStateSelector((state) => state.auth);

  const [{ isPending, isSuccess, data }, postOfferingsSearch] = useApi<
    GetOfferingsLatestRequest,
    GetOfferingsLatestResponse
  >(OfferingsAPI.buildGetOfferingsLatest());

  useEffect(() => {
    postOfferingsSearch();
  }, []);

  if (isPending) return <Loader />;

  if (!data || !isSuccess) return null;

  const { offerings, users } = data.data;

  return (
    <Container>
      <Title my={6}>Welcome, {user!.name}!</Title>

      <Box rounded='lg' bg='fg' p={4}>
        <FeedList {...{ offerings, users }} />
      </Box>
    </Container>
  );
};

export default Feed;
