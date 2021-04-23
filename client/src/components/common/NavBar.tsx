import { Button } from "@chakra-ui/button";
import { Box, Flex } from "@chakra-ui/layout";
import React from "react";
import { logout } from "../../store/actions/auth";
import useStateDispatch from "../../utils/useStateDispatch";
import Container from "./Container";
import Logo from "./Logo";
import Title from "./typography/Title";

interface NavBarProps {}

const NavBar: React.FC<NavBarProps> = ({}) => {
  const dispatch = useStateDispatch();

  return (
    <Box>
      <Container
        display='flex'
        justifyContent='space-between'
        alignItems='center'
        p={4}
      >
        <Flex alignItems='center'>
          <Logo w='75px' h='75px' />
          <Title fontSize='3.25rem' color='brand'>
            SeRa
          </Title>
        </Flex>

        <Button background='fg' onClick={() => dispatch(logout())}>
          Sign Out
        </Button>
      </Container>
    </Box>
  );
};

export default NavBar;
