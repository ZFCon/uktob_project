import React, { useState } from 'react';

function App() {
  const [inputString, setInputString] = useState('');
  const [inputNumber, setInputNumber] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate inputs
    if (!inputString.trim() || !inputNumber.trim()) {
      setError('Please enter a string and a number.');
      return;
    }

    if (isNaN(inputNumber)) {
      setError('Please enter a valid number.');
      return;
    }

    // Reset error message
    setError('');

    // Generate the repeated string
    const repeatedString = inputString.repeat(parseInt(inputNumber));

    // Update the output
    setOutput(repeatedString);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            String:
            <input
              type="text"
              value={inputString}
              onChange={(e) => setInputString(e.target.value)}
            />
          </label>
        </div>
        <div>
          <label>
            Number:
            <input
              type="text"
              value={inputNumber}
              onChange={(e) => setInputNumber(e.target.value)}
            />
          </label>
        </div>
        <button type="submit">Submit</button>
      </form>

      {error && <p className="error">{error}</p>}
      {output && <p>{output}</p>}
    </div>
  );
}

export default App;
