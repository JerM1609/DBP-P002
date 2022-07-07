export default {
  createpost: [
    {
      name: "number",
      id: 1,
      require: true,
    },
    {
      name: "id",
      id: 1,
      require: true,
    },
  ],
  createcourse: [
    {
      name: "Create",
      slug: "createcourse",
      id: 2,
      description: {
        name: "number",
        id: 1,
        require: true,
      },
    },
  ],
  updatedata: [
    {
      name: "updateData",
      slug: "updatedata",
      id: 3,
      description: {
        name: "number",
        id: 1,
        require: true,
      },
    },
  ],
};
