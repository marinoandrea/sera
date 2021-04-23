import { Action } from "redux";

interface UniqueEntity {
  id: string;
  created_at: number;
  updated_at: number;
}

export type User = {
  name: string;
  email: string;
  user_group: string;
  phone_number: string;
  is_admin: boolean;
} & UniqueEntity;

export type Offering = {
  user_account_id: string;
  category: string;
  subcategory: string;
  quantity_kg: number;
  price_per_kg_cfa_cents: number;
} & UniqueEntity;

export interface AuthState {
  isAuthenticated: boolean;
  token?: string;
  user?: User;
}

export interface ApplicationState {
  auth: AuthState;
}

export interface StateAction extends Action {
  type: string;
  payload?: any;
}

export interface SuccessResponse<T> {
  data: T;
}

export interface ErrorResponse {
  error: string;
}
