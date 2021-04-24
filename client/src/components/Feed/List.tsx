import { Table, Tbody, Td, Th, Thead, Tr } from "@chakra-ui/table";
import React from "react";
import { Offering, User } from "../../types";
import BaseText from "../common/typography/BaseText";

interface FeedListProps {
  offerings: Offering[];
  users: User[];
}

const FeedList: React.FC<FeedListProps> = ({ offerings, users }) => {
  return (
    <Table variant='striped'>
      <Thead>
        <Tr>
          <Th>Date</Th>
          <Th>Seller</Th>
          <Th>Category</Th>
          <Th>Subcategory</Th>
          <Th isNumeric>Quantity (kg)</Th>
          <Th isNumeric>CFA/kg</Th>
        </Tr>
      </Thead>
      <Tbody>
        {offerings && offerings.length > 0 ? (
          offerings
            .sort((a, b) => a.created_at - b.created_at)
            .map((offering) => {
              const user = users.find((u) => u.id === offering.user_account_id);
              if (!user) return null;
              return (
                <Tr key={offering.id}>
                  <Td>
                    {new Date(offering.created_at)
                      .toISOString()
                      .substring(0, 10)}
                  </Td>
                  <Td>{user.name}</Td>
                  <Td>{offering.category}</Td>
                  <Td>{offering.subcategory}</Td>
                  <Td isNumeric>{offering.quantity_kg}</Td>
                  <Td isNumeric>{offering.price_per_kg_cfa_cents / 100}</Td>
                </Tr>
              );
            })
        ) : (
          <BaseText>There is no data to visualize yet.</BaseText>
        )}
      </Tbody>
    </Table>
  );
};

export default FeedList;
