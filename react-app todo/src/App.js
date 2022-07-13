import logo from './logo.svg';
import './App.css';
import Todoform from './components/Todoform';
import List from './components/List';
import TodosHeader from './components/TodosHeader';

function App() {
  return (
    <div>
      <TodosHeader />
      <div className="todo-list">
      <h1>Minu ülesandeloend</h1>
      <List />
      </div>
    </div>
  );
}

export default App;
