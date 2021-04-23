import { Image } from "@chakra-ui/image";
import { Box, Flex } from "@chakra-ui/layout";
import React from "react";
import LOGO from "../../assets/logo.png";
import BaseText from "../common/typography/BaseText";
import LinkText from "../common/typography/LinkText";
import LoginForm from "./Form";

const Login: React.FC = () => {
  return (
    <Flex
      minH='100vh'
      w='full'
      direction='column'
      alignItems='center'
      justifyContent='center'
      bg='gray.100'
    >
      <Image src={LOGO} w={{ base: "sm", xl: "md" }} my={4} />
      <Box
        w={{ base: "sm", xl: "md" }}
        border='1px'
        borderColor='gray.200'
        px={{ base: 5, xl: 16 }}
        py={{ base: 6, xl: 12 }}
        bg='fg'
        rounded='lg'
      >
        <LoginForm />
      </Box>

      <BaseText py={4}>
        Don't have an account yet?
        <LinkText ml={2} to='/registration'>
          Sign Up
        </LinkText>
      </BaseText>
    </Flex>
  );
};

export default Login;
