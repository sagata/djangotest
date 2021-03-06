package cims107.dao;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.SessionFactory;

import cims107.model.Building;

public class BuildingDao {
	
	private SessionFactory sessionFactory;

	public List<Building> find(String buildingname, String departmentname, String simplename, String compus) {
		Session session = sessionFactory.openSession();
		String hql = "FROM Building AS b WHERE b.buildingname = :buildingname AND b.departmentname = :departmentname AND"
				+ "b.simplename = :simplename AND b.compus = :compus";
		Query q = session.createQuery(hql);
		
		q.setString("buildingname", buildingname);
		q.setString("departmentname", departmentname);
		q.setString("simplename", simplename);
		q.setString("compus", compus);
		
		List<Building> list = q.list();
		session.close();
		if (list.size()==0)
			return null;
		else
			return list;
	}
	
	public Building find(int buildingid) {
		Session session = sessionFactory.openSession();
		
		String hql = "FROM Building AS b WHERE b.buildingId = :buildingid";
		Query q = session.createQuery(hql);
		
		q.setString("buildingid", new Integer(buildingid).toString());
		
		List<Building> list = q.list();
		
		session.close();
		return list.get(0);
	}
	
	//检查教学楼名称是否重名
	public void add(Building building) {
		Session session = sessionFactory.openSession();
		Transaction tx = session.beginTransaction();
		session.save(building);
		tx.commit();
		session.close();
	}
	
	public void update(int buildingid, Building building) {
		
		Session session = sessionFactory.openSession();
		Transaction tx = session.beginTransaction();
		Building b = (Building) session.get(Building.class, buildingid);
		
		b.setBuildingName(building.getBuildingName());
    	b.setBuldingDepartment(building.getBuldingDepartment());
    	b.setBuildingSimpleName(building.getBuildingSimpleName());
    	b.setBuildingCompus(building.getBuildingCompus());
    	b.setBuildingFloorNum(building.getBuildingFloorNum());
    	
		session.update(b); 
		tx.commit();
		session.close();
	}
	
	public void delete(List<Integer> buildingidlst) {
		Session session = sessionFactory.openSession();
		Transaction tx = session.beginTransaction();
		/*
		for (int i = 0; i < buildingidlst.size(); i ++) {
			Building b = (Building) session.get(Building.class, buildingidlst.get(i));
			session.delete(b);
		}*/
		
		for (Iterator iter = buildingidlst.iterator(); iter.hasNext();) {
			Building temp = (Building)(iter.next());
			Building b = (Building) session.get(Building.class, temp.getBuildingId());
			session.delete(b);
		}
		
		tx.commit();
		session.close();
	}

	public SessionFactory getSessionFactory() {
		return sessionFactory;
	}

	public void setSessionFactory(SessionFactory sessionFactory) {
		this.sessionFactory = sessionFactory;
	}
}
