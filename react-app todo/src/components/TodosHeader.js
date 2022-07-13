function TodosHeader() {
  const date = new Date();
  const day = date.getDate();
  const weekDay = [
    "Pühapäev",
    "Esmaspäev",
    "Teisipäev",
    "Kolmapäev",
    "Neljapäev",
    "Reede",
    "Laupäev",
  ][date.getDay()];
  const month = [
    ". Jaanuar",
    ". Veebruar",
    ". Märts",
    ". Aprill",
    ". Mai",
    ". Juuni",
    ". Juuli",
    ". August",
    ". September",
    ". Oktoober",
    ". November",
    ". Detsember",
  ][date.getMonth()];

  return (
    <header>
      <title>Todo list</title>
      <h1 className="today" data-testid="calendar-date">
        {`${weekDay}, ${day}${month}`}
      </h1>
    </header>
  );
}

export default TodosHeader;