import { Text, TextProps } from "@chakra-ui/layout";
import React from "react";

const BaseText: React.FC<TextProps> = (props) => {
  return <Text color='text' {...props} />;
};

export default BaseText;
