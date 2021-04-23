import { Box } from "@chakra-ui/layout";
import { Spinner } from "@chakra-ui/spinner";
import React from "react";

const Loader: React.FC = () => {
  return (
    <Box p={4} mx='auto'>
      <Spinner color='brand' size='md' />
    </Box>
  );
};

export default Loader;
