def format_todo(todo):

    status = {
        0: 'NEW',
        1: 'PENDING',
        2: 'COMPLETED'
    }
    return """
    {}. {}, [{}] | Date : {} | Last Updt : {}
    _______________________________
    {}
    """.format(
        todo.id,
        todo.title,
        status[todo.status
        ],
        todo.created_at.ToDatetime(),
        todo.updated_at.ToDatetime(),
        todo.description
    )
