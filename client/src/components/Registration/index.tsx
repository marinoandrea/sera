import { Box, Flex } from "@chakra-ui/layout";
import React from "react";
import BaseText from "../common/typography/BaseText";
import LinkText from "../common/typography/LinkText";
import RegistrationForm from "./Form";

const Registration: React.FC = () => {
  return (
    <Flex
      minH='100vh'
      w='full'
      direction='column'
      alignItems='center'
      justifyContent='center'
      bg='gray.100'
    >
      <Box
        w={{ base: "sm", xl: "md" }}
        border='1px'
        borderColor='gray.200'
        px={{ base: 5, xl: 16 }}
        py={{ base: 6, xl: 12 }}
        bg='fg'
        rounded='lg'
      >
        <RegistrationForm />
      </Box>

      <BaseText py={4}>
        Already have an account?
        <LinkText ml={2} to='/'>
          Sign In
        </LinkText>
      </BaseText>
    </Flex>
  );
};

export default Registration;
