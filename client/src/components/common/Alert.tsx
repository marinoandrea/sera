import { Alert as ChakraAlert, AlertProps } from "@chakra-ui/react";
import React from "react";

const Alert: React.FC<AlertProps> = (props) => {
  const bg = `${props.status}.light`;
  const fg = `${props.status}.dark`;
  return (
    <ChakraAlert
      {...props}
      borderColor={fg}
      borderWidth={2}
      bg={bg}
      color={fg}
      rounded='md'
    />
  );
};

export default Alert;
