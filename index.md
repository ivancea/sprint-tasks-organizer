

<script>
    function calc() {
        const data = JSON.parse(document.getElementById("inputJson").value);

        try {
            validateInput(data);
        } catch (error) {
            document.getElementById("error").innerText = error;
        }
    }

    function validateInput(data) {
        if (typeof data.users !== "object") {
            throw "'users' key must be an object";
        }

        for (const user in data.users) {
            if (typeof data.users[user] !== "number") {
                throw `User '${user}' must be an array`;
            }

            if (data.users[user] < 0) {
                throw `User '${user}' must have a positive units limit`;
            }
        }

        if (typeof data.issues !== "object") {
            throw "'issues' key must be an array";
        }

        for (const issue of data.issues) {
            if (typeof issue !== "object") {
                throw "Issues must be objects";
            }

            if (typeof issue.name !== "string") {
                throw "Issues must have a 'name'";
            }

            if (typeof issue.users !== "object") {
                throw "'issues.users' must be an object";
            }

            for (const user in issue.users) {
                if (typeof issue.users[user] !== "number") {
                    throw `User '${user}' in issue must be a number`;
                }

                if (issue.users[user] < 0) {
                    throw `User '${user}' in issue must have a positive units estimation`;
                }
            }
        }
    }
</script>

<textarea id="inputJson">
{
    "users": {
        "ivancea": 5,
        "user2": 7
    },
    "issues": [
        {
            "name": "ISSUE 1",
            "users": {
                "ivancea": 2,
                "user2" 5
            }
        },
        {
            "name": "ISSUE 2",
            "users": {
                "user2": 3
            }
        },
        {
            "name": "ISSUE 3"
            "users": {
                "ivancea": 4,
                "user2": 4
            }
        }
    ]
}
</textarea>
<button onClick="calc">Calc</button>

<div id="error" style="color: red;"></div>