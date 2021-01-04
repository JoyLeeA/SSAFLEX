export default {
    User: [
      {
        user_id: 1,
        name: 'testuser1',
        created_at: '2018-09-11 11:42:11'
      },
      {
        user_id: 2,
        name: 'testuser2',
        created_at: '2018-09-11 11:42:11'
      },
      {
        user_id: 3,
        name: 'testuser3',
        created_at: '2018-09-11 11:42:11'
      },
    ],
    Content: [
      {
        content_id: 1,
        user_id: 1,
        title: '제목 1',
        context: '아직 미정입니다.',
        created_at: '2019-01-01 13:11:42',
        updated_at: null
      },
      {
        content_id: 2,
        user_id: 3,
        title: '제목 2',
        context: '아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-01-02 13:11:42',
        updated_at: null
      },
      {
        content_id: 3,
        user_id: 2,
        title: '제목 3',
        context: '아직 미정입니다. 아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-03-29 13:11:42',
        updated_at: null
      },
      {
        content_id: 4,
        user_id: 1,
        title: '제목 1',
        context: '아직 미정입니다.',
        created_at: '2019-01-01 13:11:42',
        updated_at: null
      },
      {
        content_id: 5,
        user_id: 3,
        title: '제목 2',
        context: '아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-01-02 13:11:42',
        updated_at: null
      },
      {
        content_id: 6,
        user_id: 2,
        title: '제목 3',
        context: '아직 미정입니다. 아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-03-29 13:11:42',
        updated_at: null
      },
      {
        content_id: 7,
        user_id: 1,
        title: '제목 1',
        context: '아직 미정입니다.',
        created_at: '2019-01-01 13:11:42',
        updated_at: null
      },
      {
        content_id: 8,
        user_id: 3,
        title: '제목 2',
        context: '아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-01-02 13:11:42',
        updated_at: null
      },
      {
        content_id: 9,
        user_id: 2,
        title: '제목 3',
        context: '아직 미정입니다. 아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-03-29 13:11:42',
        updated_at: null
      },
      {
        content_id: 10,
        user_id: 1,
        title: '제목 1',
        context: '아직 미정입니다.',
        created_at: '2019-01-01 13:11:42',
        updated_at: null
      },
      {
        content_id: 11,
        user_id: 3,
        title: '제목 2',
        context: '아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-01-02 13:11:42',
        updated_at: null
      },
      {
        content_id: 12,
        user_id: 2,
        title: '제목 3',
        context: '아직 미정입니다. 아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-03-29 13:11:42',
        updated_at: null
      },
      {
        content_id: 13,
        user_id: 3,
        title: '제목 2',
        context: '아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-01-02 13:11:42',
        updated_at: null
      },
      {
        content_id: 14,
        user_id: 2,
        title: '제목 3',
        context: '아직 미정입니다. 아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-03-29 13:11:42',
        updated_at: null
      },
      {
        content_id: 15,
        user_id: 3,
        title: '제목 2',
        context: '아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-01-02 13:11:42',
        updated_at: null
      },
      {
        content_id: 16,
        user_id: 2,
        title: '제목 3',
        context: '아직 미정입니다. 아직 미정입니다. 아직 미정입니다.',
        created_at: '2019-03-29 13:11:42',
        updated_at: null
      },
    ],
    Comment: [
      {
        comment_id: 1,
        user_id: 1,
        content_id: 3,
        context: '댓글 입니다.',
        created_at: '2019-03-29 14:11:11',
        updated_at: null
      },
      {
        comment_id: 2,
        user_id: 3,
        content_id: 3,
        context: '댓글 입니다.',
        created_at: '2019-03-29 16:11:11',
        updated_at: null
      },
      {
        comment_id: 3,
        user_id: 2,
        content_id: 1,
        context: '댓글 입니다.',
        created_at: '2019-03-29 14:11:11',
        updated_at: null
      }
    ],
    SubComment: [
      {
        subcomment_id: 1,
        comment_id: 3,
        user_id: 1,
        context: '댓글 입니다.',
        created_at: '2019-03-29 16:22:11',
        updated_at: null
      }
    ]
  }