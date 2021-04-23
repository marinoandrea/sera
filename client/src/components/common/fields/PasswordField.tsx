import {
  FormControl,
  FormLabel,
  IconButton,
  Input,
  InputGroup,
  InputRightElement,
} from "@chakra-ui/react";
import { useField } from "formik";
import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import FieldItem from "./FieldItem";
import InputProps from "./InputProps";

const PasswordField: React.FC<InputProps & { placeholder?: string }> = ({
  name,
  label,
  ...props
}) => {
  const [field, { error, touched }] = useField<string>(name);
  const [visible, setVisible] = useState<boolean>(false);
  return (
    <FieldItem>
      <FormControl isInvalid={!!error}>
        {label && <FormLabel htmlFor={field.name}>{label}</FormLabel>}
        <InputGroup size={props.size}>
          <Input
            variant='filled'
            bg='bg'
            {...field}
            {...props}
            type={visible ? "text" : "password"}
            id={field.name}
            isInvalid={!!error && touched}
          />
          <InputRightElement>
            <IconButton
              aria-label='visibilità'
              icon={visible ? <FaEyeSlash /> : <FaEye />}
              onClick={() => setVisible(!visible)}
            />
          </InputRightElement>
        </InputGroup>
      </FormControl>
    </FieldItem>
  );
};

export default PasswordField;
