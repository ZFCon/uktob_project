import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import App from './App';

test('repeated string is displayed correctly', () => {
  const { getByLabelText, getByText } = render(<App />);

  const stringInput = getByLabelText('String:');
  const numberInput = getByLabelText('Number:');
  const submitButton = getByText('Submit');

  fireEvent.change(stringInput, { target: { value: 'Hello' } });
  fireEvent.change(numberInput, { target: { value: '3' } });
  fireEvent.click(submitButton);

  expect(getByText('HelloHelloHello')).toBeInTheDocument();
});
