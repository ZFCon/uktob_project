import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

test('Add a new to-do item', () => {
  render(<App />);
  
  const inputElement = screen.getByPlaceholderText('Enter a new task');
  const addButtonElement = screen.getByText('Add');
  
  fireEvent.change(inputElement, { target: { value: 'Task 1' } });
  fireEvent.click(addButtonElement);
  
  expect(screen.getByText('Task 1')).toBeInTheDocument();
});

test('Add multiple to-do items', () => {
  render(<App />);
  
  const inputElement = screen.getByPlaceholderText('Enter a new task');
  const addButtonElement = screen.getByText('Add');
  
  fireEvent.change(inputElement, { target: { value: 'Task 1' } });
  fireEvent.click(addButtonElement);
  
  fireEvent.change(inputElement, { target: { value: 'Task 2' } });
  fireEvent.click(addButtonElement);
  
  expect(screen.getByText('Task 1')).toBeInTheDocument();
  expect(screen.getByText('Task 2')).toBeInTheDocument();
});

test('Delete multiple to-do items', () => {
  render(<App />);
  
  const inputElement = screen.getByPlaceholderText('Enter a new task');
  const addButtonElement = screen.getByText('Add');
  
  fireEvent.change(inputElement, { target: { value: 'Task 1' } });
  fireEvent.click(addButtonElement);
  
  fireEvent.change(inputElement, { target: { value: 'Task 2' } });
  fireEvent.click(addButtonElement);
  
  const deleteButtonElement = screen.getAllByText('Delete')[0];
  fireEvent.click(deleteButtonElement);
  
  expect(screen.queryByText('Task 1')).not.toBeInTheDocument();
  expect(screen.getByText('Task 2')).toBeInTheDocument();
});
