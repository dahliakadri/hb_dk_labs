class Homepage extends React.Component {
	render() {
        return (
            <div>
                <p>Welcome!</p>
                <a href="/cards">Friends's Cards</a>
                <br></br>
                <img src="/static/img/balloonicorn.jpg"/>
            </div>
        );
	}
}

ReactDOM.render(<Homepage />, document.getElementById('app'));