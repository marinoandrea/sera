import { Flex } from "@chakra-ui/layout";
import { Spinner } from "@chakra-ui/spinner";
import React from "react";

const Loader: React.FC = () => {
  return (
    <Flex p={4} mx='auto' maxW='sm' justifyContent='center'>
      <Spinner color='brand' size='lg' />
    </Flex>
  );
};

export default Loader;
