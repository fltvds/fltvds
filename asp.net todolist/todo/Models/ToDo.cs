using System;
using System.Collections.Generic;
using System.Linq;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;

namespace todo.Models
{
    public class ToDo
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public bool IsDone { get; set; }
        [Required]
        public string Name { get; set; }
    }
}
