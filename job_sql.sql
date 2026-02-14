CREATE DATABASE job_acceptance_db;
SELECT COUNT(*) FROM cleaned_candidates;

SELECT COUNT(*) AS total_candidates,
SUM(status) AS placed_count,
ROUND(AVG(status) * 100, 2) AS placement_rate_percentage
FROM cleaned_candidates;

SELECT company_tier_tier2,COUNT(*) AS total_candidates,
ROUND(AVG(status) * 100, 2) AS acceptance_rate_percentage
FROM cleaned_candidates
GROUP BY company_tier_tier2
ORDER BY acceptance_rate_percentage DESC;

SELECT relevant_experience_relevant,COUNT(*) AS total_candidates,
ROUND(AVG(status) * 100, 2) AS placement_rate
FROM cleaned_candidates
GROUP BY relevant_experience_relevant
ORDER BY placement_rate DESC;

SELECT skills_match_percentage,
COUNT(*) AS total_candidates,
ROUND(AVG(status) * 100, 2) AS placement_rate
FROM cleaned_candidates
GROUP BY skills_match_percentage
ORDER BY placement_rate DESC;


