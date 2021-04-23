import { Link, LinkProps } from "@chakra-ui/layout";
import React from "react";
import {
  Link as RouterLink,
  LinkProps as RouterLinkProps,
} from "react-router-dom";

const LinkText: React.FC<LinkProps & RouterLinkProps> = (props) => {
  return <Link as={RouterLink} color='brand' {...props} />;
};

export default LinkText;
