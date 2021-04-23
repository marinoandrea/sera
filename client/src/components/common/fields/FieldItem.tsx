import { useToast } from "@chakra-ui/react";
import React, { useEffect } from "react";

interface FieldItemProps {
  touched?: boolean;
  error?: string;
}

const FieldItem: React.FC<FieldItemProps> = ({
  children,
  error,
  touched = false,
}) => {
  const hasError = !!error && touched;

  const toast = useToast();

  useEffect(() => {
    if (hasError) {
      toast({
        status: "error",
        title: "Errore",
        description: error,
        position: "top",
      });
    }
    // eslint-disable-next-line
  }, [error, hasError]);

  return <>{children}</>;
};

export default FieldItem;
