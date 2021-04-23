import { Button } from "@chakra-ui/button";
import { Form, Formik } from "formik";
import React from "react";
import * as Yup from "yup";
import AuthAPI, {
  PostAuthLoginRequest,
  PostAuthLoginResponse,
} from "../../services/auth";
import { login } from "../../store/actions/auth";
import useApi from "../../utils/useApi";
import useStateDispatch from "../../utils/useStateDispatch";
import PasswordField from "../common/fields/PasswordField";
import TextInputField from "../common/fields/TextInputField";

const LoginForm: React.FC = () => {
  const dispatch = useStateDispatch();

  const [{ isPending }, postLogin] = useApi<
    PostAuthLoginRequest,
    PostAuthLoginResponse
  >(AuthAPI.buildPostLogin());

  const handleSubmit = async (values: LoginFormValues) => {
    const res = await postLogin(values);
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

          <Button
            type='submit'
            color='white'
            bgColor='brand'
            isLoading={isPending}
            mt={4}
            w='100%'
            size='lg'
          >
            Sign In
          </Button>
        </Form>
      )}
    </Formik>
  );
};

type LoginFormValues = {
  email: string;
  password: string;
};

const initialValues: LoginFormValues = {
  email: "",
  password: "",
};

const validationSchema = Yup.object({
  email: Yup.string()
    .email("Insert a valid email.")
    .required("Insert an email."),
  password: Yup.string().required("Insert a password."),
});

export default LoginForm;
