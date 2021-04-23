import { FormControl, FormLabel, Input } from "@chakra-ui/react";
import { useField } from "formik";
import React from "react";
import FieldItem from "./FieldItem";
import InputProps from "./InputProps";

const TextInputField: React.FC<
  InputProps & { type?: string; placeholder?: string }
> = ({ name, label, ...props }) => {
  const [field, { error, touched }] = useField(name);
  return (
    <FieldItem {...{ error, touched }}>
      <FormControl isInvalid={!!error && touched}>
        {label && <FormLabel htmlFor={field.name}>{label}</FormLabel>}
        <Input
          variant='filled'
          bg='bg'
          my={2}
          size='lg'
          {...field}
          {...props}
          id={field.name}
          isInvalid={!!error && touched}
          isRequired={props.required}
        />
      </FormControl>
    </FieldItem>
  );
};

export default TextInputField;
