import { Heading, HeadingProps } from "@chakra-ui/layout";
import React from "react";

const Title: React.FC<HeadingProps> = (props) => {
  return <Heading color='text' {...props} />;
};

export default Title;
