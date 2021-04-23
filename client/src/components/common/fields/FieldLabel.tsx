import { Text } from "@chakra-ui/react";
import React from "react";

const FieldLabel: React.FC = ({ children }) => (
  <Text fontWeight='bold'>{children}</Text>
);

export default FieldLabel;
