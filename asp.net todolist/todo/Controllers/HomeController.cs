using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using todo.Data;
using todo.Models;

namespace todo.Controllers
{
    public class HomeController : Controller
    {
        private readonly ApplicationDbContext _db;
        private readonly ILogger<HomeController> _logger;
        public int whatToShow = 0;
        string Search;

        public HomeController(ApplicationDbContext db)
        {
            _db = db;
        }

        public IActionResult Index(string serachPhrase)
        {
            IEnumerable<ToDo> objList = _db.ToDo;
            if (!String.IsNullOrEmpty(serachPhrase))
            {
                if (serachPhrase.Equals("1")) objList = objList.Where(t => t.IsDone);
                else if (serachPhrase.Equals("2")) objList = _db.ToDo.Where(t => !t.IsDone);
                else objList = objList.Where(t => t.Name.Contains(serachPhrase));
            }
            return View(objList);
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult showDone()
        {
            whatToShow = 1;
            return RedirectToAction("Index");
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult showUnDone()
        {
            whatToShow = 2;
            return RedirectToAction("Index");
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult showAll()
        {
            whatToShow = 0;
            return RedirectToAction("Index");
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult SwowSearchResults(string searchPhrase)
        {
            Search = searchPhrase;
            whatToShow = 3;
            return RedirectToAction("Index");
        }

        //POST - CREATE
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(ToDo obj)
        {
            if (ModelState.IsValid) {
                _db.ToDo.Add(obj);
                _db.SaveChanges();
            }
            return RedirectToAction("Index");
        }

   
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Done(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }
            var obj = _db.ToDo.Find(id);
            if (obj == null)
            {
                return NotFound();
            }

            obj.IsDone = !obj.IsDone;
            _db.ToDo.Update(obj);
            _db.SaveChanges();
            return RedirectToAction("Index");
        }

        //GET - DELETE
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }
            var obj = _db.ToDo.Find(id);
            if(obj == null)
            {
                return NotFound();
            }
            _db.ToDo.Remove(obj);
            _db.SaveChanges();
            return RedirectToAction("Index");
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
