import { Button } from "@chakra-ui/button";
import { Form, Formik } from "formik";
import React from "react";
import * as Yup from "yup";
import UsersAPI, {
  PostUsersRequest,
  PostUsersResponse,
} from "../../services/users";
import { login } from "../../store/actions/auth";
import useApi from "../../utils/useApi";
import useStateDispatch from "../../utils/useStateDispatch";
import Alert from "../common/Alert";
import PasswordField from "../common/fields/PasswordField";
import TextInputField from "../common/fields/TextInputField";

const RegistrationForm: React.FC = () => {
  const dispatch = useStateDispatch();

  const [{ isPending }, postUsers] = useApi<
    PostUsersRequest,
    PostUsersResponse
  >(UsersAPI.buildPostUsers());

  const handleSubmit = async (values: RegistrationFormValues) => {
    const res = await postUsers(values);
    if (res.isOk) dispatch(login(res.data.data));
  };

  return (
    <Formik
      {...{ initialValues, validationSchema }}
      onSubmit={handleSubmit}
      validateOnChange={false}
      validateOnBlur={false}
      validateOnMount={false}
    >
      {() => (
        <Form>
          <TextInputField
            size='lg'
            name='name'
            type='name'
            placeholder='Your name'
            required
          />

          <TextInputField
            size='lg'
            name='email'
            type='email'
            placeholder='Email'
            required
          />

          <PasswordField
            size='lg'
            name='password'
            placeholder='Password'
            required
          />

          <TextInputField
            size='lg'
            name='phone_number'
            placeholder='Your phone number'
            required
          />

          <Alert status='warning'>
            Input the number you are going to use while testing the Voxeo app.
            <br />
            Please use this format:
            <br />
            [country prefix without +][tel. number]
            <br />
            e.g. 311234567890
          </Alert>

          <Button
            type='submit'
            color='white'
            bgColor='brand'
            isLoading={isPending}
            mt={4}
            w='100%'
            size='lg'
          >
            Sign Up
          </Button>
        </Form>
      )}
    </Formik>
  );
};

type RegistrationFormValues = {
  name: string;
  email: string;
  password: string;
  phone_number: string;
};

const initialValues: RegistrationFormValues = {
  name: "",
  email: "",
  password: "",
  phone_number: "",
};

const validationSchema = Yup.object({
  name: Yup.string().required("Insert a name."),
  email: Yup.string()
    .email("Insert a valid email.")
    .required("Insert an email."),
  password: Yup.string()
    .min(3, "Please use at least 3 characters for your password.")
    .required("Insert a password."),
  phone_number: Yup.string()
    .matches(/^[0-9]+$/, "Please use the specified format for your number.")
    .required("Insert a phone number."),
});

export default RegistrationForm;
