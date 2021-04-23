import { Box, BoxProps } from "@chakra-ui/layout";
import React from "react";

const Container: React.FC<BoxProps> = (props) => {
  return <Box {...props} maxW='1024px' px={4} mx='auto' />;
};

export default Container;
